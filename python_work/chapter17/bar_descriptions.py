import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

"""一个简单的示例，它可视化前三个项目，
并给每个项目对应的条形都指定自定义标签。"""
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie','django','flask']

plot_dicts = [
	{'value': 36326, 'label': 'Description of httpie.'},
	{'value': 35536, 'label': 'Description of django.'},
	{'value': 37828, 'label': 'Description of flask.'},
	]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')