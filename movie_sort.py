import read_list
import QuickSort

url = input("Paste Letterboxd List Url and hit Enter: ")

movie_list = read_list.names_list(url)
QuickSort.sort(movie_list)
QuickSort.print_with_numbers(movie_list)
