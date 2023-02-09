
class Solution:
    def __init__(self, file_path, batch_size):
        if batch_size is None:
            self.grid_size = 500
        else:
            self.grid_size = batch_size

        self.file_path = file_path
        self.loaded_grid = []
        self.is_ended = False
        self.genz = self.open_file_n_yield()
            
    def num_islands(self):
        self.load_data()
        
        if not self.loaded_grid:
            return 0
        
        col_count = len(self.loaded_grid[0])
        count = 0
        i = 0
        j = 0
        
        while i <= len(list(self.loaded_grid)) - 1:
            while j <= col_count - 1:
                if self.loaded_grid[i][j] == '1':
                    self.dfs(i, j)
                    count += 1
                j += 1
                
            while self.is_ended == False and set(self.loaded_grid[0]) == {'0'}:
                self.loaded_grid.pop(0)
                if i >= 1:
                    i -= 1
            else:
                i += 1
            j = 0
            
            if self.is_ended == False and i >= len(list(self.loaded_grid)) - self.grid_size:
                self.load_data()
        return count


    def dfs(self, i, j):
        if i<0 or j<0 or i>=len(self.loaded_grid) or j>=len(self.loaded_grid[0]) or self.loaded_grid[i][j] != '1':
            return
        
        self.loaded_grid[i][j] = '0'
        
        self.dfs(i+1, j)
        self.dfs(i+1, j+1)
        self.dfs(i+1, j-1)
        self.dfs(i-1, j)
        self.dfs(i-1, j+1)
        self.dfs(i-1, j-1)
        self.dfs(i, j+1)
        self.dfs(i, j-1)
    
    def open_file_n_yield(self):
        ''' 
        Open file and yield one line
        '''
        with open(self.file_path, 'r', buffering=self.grid_size, newline='\n') as buffer:
            for line in buffer.readlines():
                yield list(line.strip('\n'))
    
    def load_data(self):
        try:
            counter = 0
            while counter < self.grid_size:
                self.loaded_grid.append(next(self.genz))
                counter += 1
        except:
            self.is_ended = True
            
    
def run_count_islands_script(file_path, batch_size):
    print(f"""
          Provided file_path is:
          {file_path} """)
    island_count = Solution(file_path, batch_size)
    output = island_count.num_islands()
    print(output)