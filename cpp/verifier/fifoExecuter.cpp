
#include "fifoExecuter.h"
#include "histogram.h"
#include <stdlib.h>
#include <list>
#include <algorithm>
#include <stdio.h>

#include <assert.h>

/**
 * Returns the number of enqueue operations which return before the invocation of the given remove
 * operation.
 */
int FifoExecuter::amountOfFinishedEnqueueOperations(Operation* removeOperation) const {
  int count = 0;
  Operations::Iterator iter = ops_->elements();
  for (Operation* element = iter.get(); iter.valid() && element != removeOperation; element = iter.step()) {
    if (element->type() == Operation::INSERT &&
        element->end() < removeOperation->start()) {
      count++;
    } else if (element == removeOperation) {
     break;
    }
  }
  return count;
}

int FifoExecuter::amountOfStartedEnqueueOperations(Operation* removeOperation) const {
  int count = 0;
  Operations::Iterator iter = ops_->elements();
  for (Operation* element = iter.get(); iter.valid() && element->start() <= removeOperation->end(); element = iter.step()) {
    if (element->type() == Operation::INSERT) {
      count++;
    } 
  }
  return count;
}

void FifoExecuter::execute(Histogram* histogram) {
  Operations::Iterator iter = ops_->elements();
  for (Operation* element = iter.get(); iter.valid(); element = iter.step()) {
    executeOperation(element, histogram);
  }
}

void FifoExecuter::executeOperation(Operation* element, Histogram* histogram) {
  if (element->type() != Operation::REMOVE) {
    return;
  }

  executeOperationWithOverlaps(element, histogram);
}

//int compare_operations_by_start_time(const void* left, const void* right) {
//  return (*(Operation**) left)->start() > (*(Operation**) right)->start();
//}
//
//int compare_ops_by_value(const void* left, const void* right) {
//  return (*(Operation**) left)->value() > (*(Operation**) right)->value();
//}

bool compare_by_order(Operation* left, Operation* right) {
  return left->order() < right->order();
}

void FifoExecuter::calculateOrder() {

  Operation insert_head(0, 0, 0);

  Operations::create_doubly_linked_list(&insert_head, ops_->insert_ops(), ops_->num_insert_ops());

  printf("Insert operations: \n");
    for(int i = 0; i < ops_->num_insert_ops(); i++) {
      ops_->insert_ops()[i]->print();
    }

  qsort(ops_->remove_ops(), ops_->num_remove_ops(), sizeof(Operation*), Operation::compare_operations_by_start_time);

  printf("Remove operations: \n");
  for(int i = 0; i < ops_->num_remove_ops(); i++) {
    ops_->remove_ops()[i]->print();
  }

  printf("Order: \n");
  Operations::Iterator iter = ops_->elements(&insert_head);

  int next_lin_order = 0;
  int remove_index = 0;

  for (Operation* element = iter.get(); iter.valid(); element = iter.step()) {

    std::sort(element->overlaps_insert_ops_.begin(), element->overlaps_insert_ops_.end(), compare_by_order);

    bool earlier_found;
    Operation* earlier_op;

    do {
      earlier_found = false;
      earlier_op = element;
      Time linearizable_time_window_end = element->end();
      for(size_t i = 0; i < element->overlaps_insert_ops_.size(); i++) {

        Operation* tmp = element->overlaps_insert_ops_[i];
        if(tmp->deleted()) {
          continue;
        }

        // The operation tmp is within the first overlap group, check if it should happen earlier.
        if(tmp->start() <= linearizable_time_window_end) {

          // The remove operation matching tmp occurs before the remove operation of element, so
          // tmp should happen before element.
          if(tmp->matching_op()->order() < earlier_op->matching_op()->order()) {
            earlier_op = tmp;
            earlier_found = true;
          }

          // Adjust the the end of the first overlap group.
          if(tmp->end() < linearizable_time_window_end) {
            linearizable_time_window_end = tmp->end();
          }
        }
      }

      // Remove first all remove operations which started before the earliest insert operation
      // still in the list.
      while(remove_index < ops_->num_remove_ops() && ops_->remove_ops()[remove_index]->start() < earlier_op->start()) {
        ops_->remove_ops()[remove_index]->set_lin_order(next_lin_order);
        ops_->remove_ops()[remove_index]->print();
        next_lin_order++;
        remove_index++;

      }

      // Remove the insert operation.
      earlier_op->set_lin_order(next_lin_order);
      next_lin_order++;
      earlier_op->remove();
      earlier_op->print();
    }
    while(earlier_found);
  }

  // Remove all remaining remove operations.
  for (; remove_index < ops_->num_remove_ops(); remove_index++) {
    ops_->remove_ops()[remove_index]->set_lin_order(next_lin_order);
    next_lin_order++;
    ops_->remove_ops()[remove_index]->print();
  }
}

//  void Operation::determineExecutionOrderLowerBound(Operations& ops,
//      FifoExecuter* executer, int errorDistance,
//      vector<ErrorEntry>* result) const {
//    Time linearizable_time_window_end = end();
//    for (size_t i = 0; i < overlaps_.size(); i++) {
//      Operation* element = *ops[overlaps_[i]];
//      if (element->start() < linearizable_time_window_end) {
//        // AH: What is element->delete? It is not mentioned in the documentation of the function.
//        if (!element->deleted() && element->value() != -1
//            && element->type() == REMOVE) {
//          Operation* matchingInsert;
//          int errorDistanceTmp = executer->semanticalError(element,
//              &matchingInsert);
//          if (errorDistanceTmp < errorDistance) {
//            ErrorEntry e(element, errorDistanceTmp, matchingInsert);
//            result->push_back(e);
//          }
//          if (element->end() < linearizable_time_window_end) {
//            linearizable_time_window_end = element->end();
//          }
//        }
//      } else {
//        break;
//      }
//    }
//    sort(result->begin(), result->end(), compOpLowerBound);
//  }

//  Operation** insert_ops = new Operation*[];
//    Operation** remove_ops = new Operation*[num_operations_];
//    int insert_index = 0;
//    int remove_index = 0;
//    for (int i = 0; i < num_operations; i++) {
//      if (ops[i]->type_ == Operation::INSERT) {
//        insert_ops[insert_index] = ops[i];
//        insert_index++;
//      } else {
//        remove_ops[remove_index] = ops[i];
//        remove_index++;
//      }
//    }
