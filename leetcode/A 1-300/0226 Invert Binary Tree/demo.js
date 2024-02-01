function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right(right === undefined ? null : right)
}


/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function (root) {
    if (root == null) {
        return null
    }
    let temp = invertTree(root.left)
    root.left = invertTree(root.right)
    root.right = temp
    return root
}