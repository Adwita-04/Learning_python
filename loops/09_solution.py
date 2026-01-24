items=["apple","bnana","mango","pineapple","guvava","apple","orange","mango"]

unique_item=set()

for item in items:
    if item in unique_item:
        print("duplicate item :" ,item)
        break
    else:
        unique_item.add(item)