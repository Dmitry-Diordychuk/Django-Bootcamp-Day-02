#!/usr/bin/python3
# coding: utf-8


import sys
import os
import re
import settings


def generate_output_filename(template_filename_parts):
    template_filename_parts[-1] = "html"
    output_filename = ""
    for part in template_filename_parts:
        output_filename += part + '.'
    output_filename = output_filename[:-1]
    return output_filename


def insert_vars(template):
    while True:
        left_brace_index = template.find("{")
        right_brace_index = template.find("}")
        if left_brace_index == -1 or right_brace_index == -1 \
           or left_brace_index > right_brace_index:
            break
        key = template[left_brace_index + 1:right_brace_index]

        try:
            value = getattr(globals()["settings"], key)
        except AttributeError as attr_ex:
            raise attr_ex

        template = template.replace("{" + key + "}", str(value))
    return template


def run():
    if len(sys.argv) != 2:
        raise ValueError("Wrong number of arguments!\nfilename.template is required.")

    filename = sys.argv[1]
    filename_parts = filename.split('.')
    if filename_parts[-1] != "template":
        raise ValueError("Wrong file format!\nfilename.template is required.")

    template = ""
    try:
        with open(filename) as file:
            for line in file:
                template += line
    except OSError as os_ex:
        raise os_ex

    html_page = insert_vars(template)

    output_file = generate_output_filename(filename_parts)

    try:
        with open(output_file, 'w+') as file:
            file.write(html_page)
    except OSError as os_error:
        raise os_error


if __name__ == '__main__':
    try:
        run()
    except Exception as error:
        print("Error: {0}".format(error))
