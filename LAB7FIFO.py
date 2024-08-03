def pageFaults(pages, n, capacity):
    # To represent the current pages in memory in the order of FIFO
    current_pages = [-1] * capacity  # Initialize with an invalid page number
    index = 0  # To keep track of the position to replace in FIFO manner
    page_faults = 0

    for i in range(n):
        if pages[i] not in current_pages:
            # Page fault occurs if the page is not in memory
            page_faults += 1
            
            # Replace the oldest page with the new page
            current_pages[index] = pages[i]
            index = (index + 1) % capacity  # Move to the next position in a circular manner
            print(f"Page {pages[i]} added. Current pages in memory: {current_pages}")
        else:
            print(f"Page {pages[i]} is already in memory. Current pages in memory: {current_pages}")
        
    return page_faults

# Driver code
if __name__ == '__main__':
    pages = [6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 2, 0]
    n = len(pages)
    capacity = 3
    print("Total page faults:", pageFaults(pages, n, capacity))
