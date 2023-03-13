#include "lists.h"
/**
 * is_palindrome - function that check for palindrom
 * @head:list
 *Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	const listint_t *current;
	int len;
	int i, j;
	int arr[10000];

	if (*head == NULL)
		return (1);
	current = *head;
	len = 0;
	while (current != NULL)
	{
		current = current->next;
		len++;
	}
	if (len == 1)
		return (1);

	current = *head;
	i = 0;
	while (current != NULL)
	{
		arr[i] = current->n;
		i++;
		current = current->next;
	}
	j = 0;
	i--;
	len--;
	while (i >= (len / 2))
	{
		if (arr[i] != arr[j])
			return (0);
		i--;
		j++;
	}
	return (1);
}

