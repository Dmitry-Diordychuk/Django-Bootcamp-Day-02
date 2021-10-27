#!/usr/bin/python3
# coding: utf-8
from elem import Elem, Text


class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='html', attr=attr, content=content)

class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='head', attr=attr, content=content)

class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='body', attr=attr, content=content)

class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='title', attr=attr, content=content)

class Meta(Elem):
	def __init__(self, attr={}):
		super().__init__(tag='meta', attr=attr, tag_type='simple')

class Img(Elem):
	def __init__(self, attr={}):
		super().__init__(tag='img', attr=attr, tag_type='simple')

class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='table', attr=attr, content=content)

class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='th', attr=attr, content=content)

class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='tr', attr=attr, content=content)

class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='td', attr=attr, content=content)

class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='ul', attr=attr, content=content)

class Ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='ol', attr=attr, content=content)

class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='li', attr=attr, content=content)

class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='h1', attr=attr, content=content)

class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='h2', attr=attr, content=content)

class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='p', attr=attr, content=content)

class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='div', attr=attr, content=content)

class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__(tag='span', attr=attr, content=content)

class Hr(Elem):
	def __init__(self, attr={}):
		super().__init__(tag='hr', attr=attr, tag_type='simple')

class Br(Elem):
	def __init__(self, attr={}):
		super().__init__(tag='br', attr=attr, tag_type='simple')

if __name__ == '__main__':
	print(Html(attr={'lang':'en'}))
	print(Head())
	print(Body())
	print(Title())
	print(Meta())
	print(Img())
	print(Table())
	print(Th())
	print(Tr())
	print(Td())
	print(Ul())
	print(Ol())
	print(Li())
	print(H1())
	print(H2())
	print(P())
	print(Div())
	print(Span())
	print(Hr())
	print(Br())

	print('--My example--')
	print(
		Html([
			Head([
				Meta(attr={'charset':'UTF-8'}),
				Title(Text('\\"My site\\"'))
			]),
			Body([
				Div([
					H1(Text('\\"Article title\\"')),
					P([
						Text('\\"Some text1\\"'),
						Hr(),
						Text('\\"Text continues\\"')
					], {'style':'color: blue;'}),
					Img(attr={'src':'http://i.imgur.com/pfp3T.jpg'})
				]),
				Table([
					Tr([Th(Text(1)), Td(Text(2)), Td(Text(3))]),
					Tr([Th(Text(4)), Td(Text(5)), Td(Text(6))]),
					Tr([Th(Text(7)), Td(Text(8)), Td(Text(9))])
				], {'style':'table-layout: fixed; width: 100%; \
					border-collapse: collapse; border: 3px solid purple;'})
			])
		], attr={'lang':'en'})
	)

	print('--Subject example--')
	print(
		Html(
			[
			Head(
				Title(Text('\\"Hello ground!\\"'))
			),
			Body(
				[
				H1(Text('\\"Oh no, not again!\\"')),
				Img(attr={'src':'http://i.imgur.com/pfp3T.jpg'})
				]
			)
			]
		)
	)
