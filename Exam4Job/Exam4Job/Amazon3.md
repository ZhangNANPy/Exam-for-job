#亚马逊第三题：

每一个部长有一个正效率值。法庭的效率值是法庭中所有部长的效率值之和。国王要从法庭中移除一些部长，他要求部长给处自己以外的部长投票，若A投给B“YES”，代表A想要B留在法庭；若A投给B“NO”，代表A不想要B留在法庭。

部长间达成了一些协议。协议有如下形式“如果我投给你YES，你要同样给我YES”。国王注意到了这些，并因此要选出一个新的部长集团，过完遵循以下守则来选这个集团：
如果部长A被选出，被他投YES的部长都会被拒绝。
在这一规则下，选出最大法院效率的部长集团。

###目标：
找出最大法院效率。

###输入：3个参数
numOfMin 部长的数目
efficiency 一个整数列表，表示部长们的效率
voteInFavour 一个喜好的列表，每一个喜好是一个有两个整数的列表，表明了这两个部长会互相投YES

###输出：最大法院效率