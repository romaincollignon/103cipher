##
## EPITECH PROJECT, 2022
## 103cipher
## File description:
## Makefile
##

SRC			:= 103cipher.py

NAME		=	103cipher

.PHONY:		all
all:		$(NAME)
$(NAME):
			cp $(SRC) $(NAME)
			chmod +x $(NAME)

.PHONY:		clean
clean:
			$(RM) -rf src/__pycache__ .coverage

.PHONY:		fclean
fclean:		clean
			$(RM) $(NAME)

.PHONY:		re
re:			fclean all
