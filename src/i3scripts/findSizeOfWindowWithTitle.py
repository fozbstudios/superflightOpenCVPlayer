import i3ipc
#get i3 obj
i3 = i3ipc.Connection()
tree=i3.get_tree()
wind=tree.find_named(".*master.*")
print(wind[0].name)
print(wind[0].id)
print(str(wind[0].window_rect.x)+" "+str(wind[0].window_rect.y)+" "+str(wind[0].window_rect.width)+" "+str(wind[0].window_rect.height)+" ")
