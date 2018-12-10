def classify(tree, feature):
    # recursively call the tree until a concrete class is returned
    k = list(tree.keys())[0]
    item = tree[k]
    ret = item[feature[k]]
    if isinstance(ret, dict):
        return classify(ret, feature)
    else:
        return ret


if __name__ == '__main__':
    tree = {1: {0: {0: {0: 'not bad', 1: 'not good'}}, 1: {0: {0: 'bad', 1: 'medium'}}}}
    a1 = [0, 1]
    a2 = [0, 0]
    print(classify(tree, [0, 0]))
    print(classify(tree, [0, 1]))
    print(classify(tree, [1, 0]))
    print(classify(tree, [1, 1]))
