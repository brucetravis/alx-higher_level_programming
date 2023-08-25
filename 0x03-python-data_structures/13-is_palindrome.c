#include "lists.h"
#include <stddef.h>

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to a pointer to the head of the linked list.
 * Return: 1 if it's a palindrome, 0 if it's not.
 */
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
