#!/usr/bin/python3
# coding: utf-8
from elements import *


class Page():
	def __init__(self, element):
		if not isinstance(element, Elem):
			raise ValueError("element parameter must inheriting from Elem")
		self.root = element

	def __str__(self):
		if isinstance(self.root, Html):
			return "<!DOCTYPE html>\n" + str(self.root)
		return str(self.root)

	def write_to_file(self, filename):
		try:
			with open(filename, 'w+') as file:
				file.write(self.__str__())
		except OSError as os_error:
			raise os_error

	def is_valid(self):
		if isinstance(self.root, Html):
			return self.__check_html(self.root)
		elif isinstance(self.root, Head):
			return self.__check_head(self.root)
		elif isinstance(self.root, Body) or isinstance(self.root, Div):
			return self.__check_body_or_div(self.root)
		elif isinstance(self.root, Title)\
			or isinstance(self.root, H1)\
			or isinstance(self.root, H2)\
			or isinstance(self.root, Li)\
			or isinstance(self.root, Th)\
			or isinstance(self.root, Td)\
			or isinstance(self.root, P):
			return self.__check_text_elem(self.root)

		return False

	def __check_html(self, html):
		html_content = html.content
		if len(html_content) < 2:
			return False
		head = html_content[0]
		body = html_content[1]
		if not isinstance(head, Head)\
		  and not isinstance(body, Body):
		   return False
		return True\
			and self.__check_head(head)\
			and self.__check_body_or_div(body)

	def __check_head(self, head):
		head_content = head.content
		title_counter = 0
		for el in head_content:
			if isinstance(el, Title):
				if not self.__check_text_elem(el):
					return False
				title_counter += 1
		if title_counter != 1:
			return False
		return True

	def __check_body_or_div(self, elem):
		elem_content = elem.content
		for el in elem_content:
			if isinstance(el, H1)\
				or isinstance(el, H2):
				if (not self.__check_text_elem(el)):
					return False
			elif isinstance(el, Div)\
				or isinstance(el, Table)\
				or isinstance(el, Ul)\
				or isinstance(el, Ol)\
				or isinstance(el, Span)\
				or isinstance(el, Text):
				continue
			else:
				return False
		return True

	def __check_text_elem(self, elem):
		elem_content = elem.content
		if len(elem_content) != 1:
			return False
		if not isinstance(elem_content[0], Text):
			return False
		return True

	def __check_span(self, span):
		span_content = span.content
		for el in span_content:
			if isinstance(el, Text) or isinstance(el, P):
				if not self.__check_text_elem(el):
					return False
			else:
				return False
		return True

	def __check_list(self, list):
		if len(list.content) < 1:
			return False
		for el in list.content:
			if isinstance(el, Li) or isinstance(el, Li):
				if not self.__check_text_elem(el):
					return False
			else:
				return False
		return True

	def __check_tr(self, tr):
		if len(tr.content) < 1:
			return False
		th_flag = False
		td_flag = False
		for el in list.content:
			if th_flag and td_flag:
				return False
			if isinstance(el, Th):
				th_flag = True
			elif isinstance(el, Td):
				td_flag = True
			else:
				return False
			if not self.__check_text_elem(el):
				return False
		return True

	def __check_table(self, table):
		for el in table.content:
			if isinstance(el, Tr):
				if not self.__check_tr(el):
					return False
			else:
				return False
		return True


if __name__ == '__main__':
	page = Page(Html([
		Head([
			Title(Text('\\"My site\\"'))
		]),
		Body([
			Div([
				H1(Text('\\"Article header\\"'))
			])
		])
	]))
	print(page)
	print(page.is_valid())
	page.write_to_file("mypage.html")
