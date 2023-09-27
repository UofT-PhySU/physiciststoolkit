"""Primarily for editing LaTeX files."""
import csv

def convert_csv(file_name):
    """This function reads csv tables and converts them to LaTeX source codes that
    can be directly copied and pasted into LaTeX files.

    Args:
        file_name (str): The name of the csv file.
    
    Returns:
        None
    """
    begin_table = r'\begin{table}[H]' + '\n' + '    \centering' + '\n'
    begin_table += '    \caption{}' +'\n' + '    \\begin{tabular}[H]'

    with open(f'{file_name}', mode = 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        speci_cha = r'_^\\'
        content = []

        for row in reader:
            counter = 0
            for item in row:
                if any(cha in item for cha in speci_cha):
                    row[counter] = f'\({row[counter]}\)'
                counter += 1
            content.append(' '*8 + ' & '.join(row))

        col_def = "{" + "|l" * len(row) + "|}" + '\n' + ' ' * 8 + '\hline'

    data = (r'\\ \hline' + '\n').join(content) + r'\\ \hline' + "\n"
    begin_table += col_def + '\n'
    end_table = "    \end{tabular}" + "\n" + r'\end{table}'

    print ('\n' + begin_table + data + end_table)
