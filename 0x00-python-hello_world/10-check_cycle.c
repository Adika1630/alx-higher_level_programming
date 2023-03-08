#include "lists.h"

/**
 * check_cycle - list
 * @head:  type list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t fast, slow;

	if (head == NULL || head->next == NULL)
		return (0);

	while (slow && fast && fast->next)
	{
		if (fast == slow)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
