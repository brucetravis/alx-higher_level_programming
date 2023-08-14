#include <stddef.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
int n;
struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head)
{
if (*head == NULL || (*head)->next == NULL)
return (1);
	
listint_t *slow = *head;
listint_t *fast = *head;

while (fast && fast->next)
{
slow = slow->next;
fast = fast->next->next;
}

listint_t *prev = NULL;
listint_t *current = slow;
listint_t *next;

while (current)
{
next = current->next;
current->next = prev;
prev = current;
current = next;
}

listint_t *first = *head;
listint_t *second = prev;

while (second)
{
if (first->n != second->n)
return (0);

first = first->next;
second = second->next;
}

return (1);
}
