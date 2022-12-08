class Dir:
    def __init__(self,parent,name) -> None:
        self.parent=parent
        self.name=name
        self.children=[]
        self.file_sizes=0
        self.list=False


    def cd(self,arg):
        if arg == "..":
            return self.parent

        if arg == "/":
            if self.parent is None:
                return self
            else:
                return self.parent.cd("/")

        for child in self.children:
            if child.name == arg:
                return child

        self.children.append(Dir(self,arg))
        return self.children[-1]

    def parse_ls(self,lines):
        if self.list:
            return

        for line in lines:
            if line.startswith("dir"):
                self.children.append(Dir(self,line.replace("dir ","").replace("\n","")))
            else:
                self.file_sizes+=int(line.split(" ")[0])
        
        self.list=True


    def add(self,size):
        self.file_sizes+=size

    def get_size(self):
        child_size=0
        for child in self.children:
            child_size+=child.get_size()

        return self.file_sizes + child_size


    def sum_dirs_lt(self,thresh=100000):
        s=0
        if self.get_size() <= thresh:
            s+=self.get_size()
        for child in self.children:
            s+=child.sum_dirs_lt(thresh=thresh)
        return s

    def get_all_sizes(self):
        l=[self.get_size()]
        for child in self.children:
            l.extend(child.get_all_sizes())

        return l


root_node=Dir(None,"/")
ak_node=root_node
with open('input.txt') as f:
    lines=f.readlines()
    i=0
    while i < len(lines):
        line=lines[i]
        if line.startswith("$ cd"):
            ak_node=ak_node.cd(line.replace("$ cd ","").replace("\n",""))
        elif line.startswith("$ ls"):
            i+=1
            lslines=[]
            while i < len(lines) and not lines[i].startswith("$"):
                lslines.append(lines[i])
                i+=1
            ak_node.parse_ls(lslines)
            i-=1

        i+=1

print(root_node.sum_dirs_lt())

all_sizes=sorted(root_node.get_all_sizes())
needed_space=30000000-(70000000-root_node.get_size())

i=0
while i < len(all_sizes) and all_sizes[i]< needed_space:
    i+=1
print(all_sizes[i])
