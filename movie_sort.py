import read_list
import QuickSort

url = input("Paste Letterboxd List Url and hit Enter: ")
movie_list = names_list(url)
QuickSort.quick_sort(movie_list)
QuickSort.print_with_names(movie_list)
