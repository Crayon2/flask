<h1> Readme.md技术文档之总结说明</h1>

> 代码仓库：[Github URL]( https://github.com/Crayon2/flask)

> Pythonanywhere URL：[作者刘瑜鹏]( http://crayon3.pythonanywhere.com/)、[18级伙伴刘宇](http://liuyu18.pythonanywhere.com/)

> 项目说明文档：[说明文档_URL]( https://github.com/wenjunmo/DataStory_Interactive-Visualization/blob/master/README.md)

#### 本项目是与17级师兄莫文俊一起合作的web应用，主题为“世界500强公司折射的全球经济结构分析”，在flask环境下，导入pandas、plotly、cufflinks、pyecharts模块，实现了数据的筛选与图表的交互。

##### 下面是各个文档说明：

<h3> Web APP动作描述</h3>

首页下拉框可以对各个国家（country）进行筛选，点击“do it”提交按钮，分别跳转到“/hurun”页面，可以看到对应的图形与表格信息，图形能够实现交互，即把光标放在上面，能够显示所对应的信息（公司名称与收益）。图形是有关本筛选国家各个公司（company）于2019年的收益（profit），从中我们可以看出筛选国家所占世界500强公司的名称以及其他详细的信息。

在首页下方还有一个“结论”按钮，点击按钮可以跳转到总结页面“/render”，在这个页面里，有“bar_base，wordcloud_diamond，map_world，table_base”四个导航按钮，分别对应的是“世界500强排名”，“WorldCloud-shape-diamond”,“Map-世界地图”，“Table”图表，以不同的图形向我们展示各个国家在世界500强里所占有的公司的数量，每一张图行都能够实现联动，使我们更加清晰的了解全球经济结构，从趋势上看，我们还会发现，小国想要产生 “100 强” 或许会越来越难；而拥有较多 100 强企业的中国和美国，则很可能会产生更多的 100 强，尤其是中国的势头强劲，增速远远超过美国。

<h3>HTML档描述-templates</h3>

**results2.html**

是首页下拉框进行选择所要筛选的国家而后跳转的页面，用两个表单form分别表示下拉框的选项选择及其按钮，和跳转到结论页面“render.html”的按钮“结论”。

在这个页面还需要引入css，以link标签插入样式的URL。＜link href="../static/hf.css" rel="stylesheet"/＞（样式的URL通常是放在static文件夹中，这个文件夹与templates，py文件和数据文件是同级的。）

在页面主标题处，我是以一个＜header＞标签插入的，设置好width和height，还要设置位置，我这里要求水平居中，对样式的定义为{margin-right: auto;margin-left: auto;}，如果需要上下留出空位的话，同样对margin-top（外边距高），margin-bottom（外边距底）进行定义。

在页面中，我还插入了两个表单，一个放下拉框和确认按钮，一个放跳转总结页面的按钮。

定义下拉框的标签为＜select＞，select 元素可创建单选或多选菜单。＜select&＞ 元素中的 ＜option＞ 标签用于定义列表中的可用选项。而＜option＞ 标签中的内容作为 select 标签的菜单或是滚动列表中的一个元素显示。

用if语句对下拉框的选项进行筛选，在列表the_region_selected中，选择符合条件的‘item’。

对于按钮，是采用input元素，类型定义为'SUBMIT'

表单 ＜form＞ 标签用于为用户输入创建 HTML 表单。能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。

表单 ＜form＞ 的method 属性设置的方法共有两种方法：POST 方法和 GET 方法。

如果采用 POST 方法，浏览器将会按照下面两步来发送数据。首先，浏览器将与 action 属性中指定的表单处理服务器建立联系，一旦建立连接之后，浏览器就会按分段传输的方法将数据发送给服务器。

在服务器端，一旦 POST 样式的应用程序开始执行时，就应该从一个标志位置读取参数，而一旦读到参数，在应用程序能够使用这些表单值以前，必须对这些参数进行解码。用户特定的服务器会明确指定应用程序应该如何接受这些参数。

另一种情况是采用 GET 方法，这时浏览器会与表单处理服务器建立连接，然后直接在一个传输步骤中发送所有的表单数据：浏览器会将数据直接附在表单的 action URL 之后。这两者之间用问号进行分隔。

一般浏览器通过上述任何一种方法都可以传输表单信息，而有些服务器只接受其中一种方法提供的数据。可以在 <form> 标签的 method （方法）属性中指明表单处理服务器要用方法来处理数据，使 POST 还是 GET。

我在第一个表单中，即下拉框和其提交按钮，使用的方法为‘POST’，并且将表单数据提交到名为 "hurun" 的页面. 

第二个表单中，method 属性为'GET','POST'，因为我发现在某些浏览器中，利用其中某个方法页面跳转不出来，因而我将两种方法一起写上。

在body最后，{{ the_plot_all|safe }}----交互图表，（jinjia2语法的动态数据绑定，在py文件中有对应的可视化函数传输数据）{{ the_res|safe }}---数据表格

**render.html**

结论页面，主要呈现的是pyechart图表，加入导航tab，可以实现四个交互图表的跳转。在render.html中，除了导航和图表（pyechart是17级前辈做的，我也不太清楚是怎么生成的图表），我还插入了一个写总结的div盒子。其中为了使页面更加好看，我对div盒子的边框属性进行改造，利用border-radius改变了传统盒子的棱角，使其变为圆滑的曲线，使div盒子看起来不那么生硬，更加符合现代审美

<h3> Python档描述</h3>

**环境**：flask环境

**安装模块**：pandas、plotly、cufflinks、pyecharts模块

**导入csv数据文档**,pandas 大法读内容, 用dropna()丢缺失值, 用unique()取唯一值,使取值 不重覆

df = pd.read_csv('xxx.csv', encoding='gbk')编码encoding我用的是” GBK” GBK是采用单双字节变长编码，英文使用单字节编码，完全兼容ASCII字符编码，中文部分采用双字节编码。

regions_available_loaded = list(df.xx.dropna().unique())---xx是你自己想要筛选的数据总名称。

Route路由，我写了三个，一个源页面，一个路径为hurun的页面，一个路径为render的页面

源页面，@app.route('/'),”/”是URL，也就是这一个页面对应的是首页，即一开始进入项目的页面，这个页面主要是return到“results.html” 

@app.route('/hurun')包含前端页面（这里是results.html）需要呈现的数据

the_region = request.form["the_region_selected"]----这里的"the_region_selected"对应的是results2.html文档中的select下拉框中的选项；

dfs = df.query("xx=='{}'".format(the_region))—xx即你想要筛选数据的总名称，与前面“regions_available_loaded”中的xx是一致的；

fig = dfs.iplot(kind="bar", x="aa",y="bb",asFigure=True),aa和bb是x轴和y轴的数据名称，比如我自己x轴上写的是“company”即x 轴每个单位点代表的是各个公司，y轴写的是“profit”，即各个公司对应的收益；

py.offline.plot(fig, filename="example1.html",auto_open=False)--plotly图像整体属性设置复制代码，example1则是放置代码的文件，这个HTML文档放在templates文件夹中，它也会自动生成一个与templates同级的文件，因而我就没有把它放在templates文件夹中。

利用with语句打开文件（example1.html），调用plotly模块绘图，并将其通过the_plot_all传输到results2.html页面中

@app.route('/render')web应用增加总结页面render.html

<h3> 总结感言: </h3>

本次项目是我第一次与不同年级的前辈一起合作，通过本次合作，我体会到了什么是产品经理的角色，什么是开发人员的角色，项目是要通过共同参谋，共同讨论做出来的，通过别人的看法，完善自己的项目，通过别人的技术，完善自己的项目；在这其中我学会了很多东西，也有很多的感悟。这似乎与社会上公司的分工合作相同，提前体会到这种模式，或许对以后我步入社会工作有所帮助。


