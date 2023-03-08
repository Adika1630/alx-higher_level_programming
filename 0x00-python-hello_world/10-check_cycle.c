#include "lists.h"

/**
 * check_cycle - list
 * @head:  type list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *head)
{
	listint_t *nextn = head, *nextn_nextn = head;

	while (nextn && nextn_nextn  && nextn_nextn->next)
	{
		nextn = nextn->next;
		nextn_nextn  = nextn_nextn->next->next;
		if (nextn == nextn_nextn)
		{
			return (1);
		}
	}
	return (0);
}
