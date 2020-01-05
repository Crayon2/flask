from flask import Flask, render_template, request
import pandas as pd
import cufflinks as cf
import plotly as py
import plotly.graph_objs as go
from pyecharts import options as opts
from pyecharts.charts import Line



df1 = pd.read_csv("oneenergy.csv",encoding='gbk')


app = Flask(__name__)

# 准备工作

regions_available = list(df1.country.dropna().unique())




@app.route('/',methods=['GET'])
def hu_run_2019():
    data_str = df1.to_html()
    return render_template('results2.html',
                           the_res = data_str,
                           the_select_region=regions_available)

@app.route('/hurun',methods=['POST'])
def hu_run_select() -> 'html':
    the_region = request.form["the_region_selected"]
    print(the_region) # 检查用户输入
    dfs = df1.query("country=='{}'".format(the_region))

    fig = dfs.iplot(kind="bar", x="company",y="profit",asFigure=True)
    py.offline.plot(fig, filename="example1.html",auto_open=False)
    with open("example1.html", encoding="utf8", mode="r") as f:
        plot_all = "".join(f.readlines())

    data_str = dfs.to_html()
    return render_template('results2.html',
                            the_plot_all = plot_all,
							# the_plot_all = [],
                            the_res = data_str,
                            the_select_region=regions_available,
                           )

@app.route('/render')
def entry_page() -> 'html':
    return render_template('render.html',
                           the_title='Welcom to search4letters on the web')


if __name__ == '__main__':
    app.run(debug=True,port=8000)
