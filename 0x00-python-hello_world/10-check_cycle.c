#include "lists.h"

/**
 * check_cycle - list
 * @head:  type list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	int *node1, *node2;

	if (head == NULL)
		return (0);

	while (head != NULL)
	{
		node1 = (int *)&head;
		node2 = (int *)&head->next;
		if (head->next == NULL)
			return (0);

		if (*node1 - *node2 <= 0)
			return (1);

		head = head->next;
	}
	return (0);
}
