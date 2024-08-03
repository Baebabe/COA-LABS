# LRU PAGE REPLACEMENT
def pageFaults(pages, n, capacity): 
    s = [] 
    indexes = {} 
    page_faults = 0
    
    for i in range(n): 
        if pages[i] not in s: 
            if len(s) < capacity: 
                s.append(pages[i])  
                page_faults += 1
                print(f"Adding {pages[i]} : {s}")
            else: 
                lru = float('inf') 
                val = None
                for page in s: 
                    if indexes[page] < lru: 
                        lru = indexes[page] 
                        val = page 
                s[s.index(val)] = pages[i]  
                page_faults += 1
                print(f"Replacing {val} with {pages[i]} : {s}")
        else:
            print(f"Accessing {pages[i]} : {s}")

        indexes[pages[i]] = i 
    
    return page_faults 

pages = [6, 1, 1, 2, 0, 3, 4, 6, 0, 2, 1, 2, 1, 2, 0, 3, 2, 1, 2, 0]  
n = len(pages) 
capacity = 3
print(f"Total Page Faults: {pageFaults(pages, n, capacity)}")

