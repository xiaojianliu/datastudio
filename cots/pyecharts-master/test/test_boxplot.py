from unittest.mock import patch

from nose.tools import eq_

from pyecharts.charts import Boxplot


@patch("pyecharts.render.engine.write_utf8_html_file")
def test_boxpolt_base(fake_writer):
    v1 = [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790],
    ]
    v2 = [
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870],
    ]
    c = Boxplot()
    c.add_xaxis(["expr1", "expr2"]).add_yaxis("A", c.prepare_data(v1)).add_yaxis(
        "B", c.prepare_data(v2)
    )
    c.render()
    _, content = fake_writer.call_args[0]
    eq_(c.theme, "white")
    eq_(c.renderer, "canvas")
