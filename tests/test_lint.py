from ora_lint import lint

def test_select_star():
    f=lint("select * from customers")
    assert f[0].rule=="ORA001"

def test_when_others_null():
    f=lint("begin null; exception when others then null; end;")
    assert any(x.rule=="ORA002" for x in f)
