#include <stdio.h>
#include <malloc.h>
#include<omp.h>
#include <math.h>
#include<stdlib.h>

struct node {

    int data;
    struct node *next;
};

void create_linked_list(struct node **root_ptr, int count) {
    
    struct node **curr_ptr = root_ptr;
    struct node *curr = NULL;

    #pragma omp parallel
    {    
        #pragma omp sections
        {
            for (int i = 0; i < count; i++) {

            *curr_ptr = (struct node *)malloc(sizeof(struct node *));
            curr = *curr_ptr;
            curr->data = i + 1;
            curr->next = NULL;
            curr_ptr = &(curr->next); 
        } 
        
    }
    
}

void print_linked_list(struct node *root) {

    #pragma omp parallel 
    {
        
        #pragma omp sections
        {
            for(struct node *curr = root; curr != NULL; curr = curr->next) {
    
                printf("Data: %d\n", curr->data); 
            } 
        }
    }
    
}

void print_linked_list_fib(struct node *root) {
    
    struct node *curr = root;
    int old_val = 1;
    printf("Data: %d\n", curr->data);
    int curr_val = 1;
    int i = 0;
    int j=0;
    curr = curr->next;

    #pragma omp parallel 
    {    
        #pragma omp sections
        {
            for(struct node *curr = root; curr != NULL; curr = curr->next) {
    
                if (i == old_val) {

                    old_val = curr_val;
                    curr_val = curr_val + i;
                    i = 0;
                    printf("Data: %d\n", curr->data);
                }
                i++; 
            }
        }
    }
}

int main() {

    struct node *root = NULL;
    const int count = 20;
    create_linked_list(&root, count);
    printf("\n\nList of all nodes\n");
    print_linked_list(root); 
    printf("\n\nList of fibonacci nodes\n");
    print_linked_list_fib(root);
    return 0;
}