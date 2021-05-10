{% extends 'base.html' %}
{% block title%}{{ title }}{% endblock %}
{% block content %}
<div class="main">
<div class="leftTop">
    <a href="javascript:void(0);" onclick="dark()">
        <i data-feather="sun"></i>
    </a>
</div>
<div>
    <h1 class="h1">
        <span>Cat VS Dog <small>1.0.0</small></span>
    </h1>
    <h3 class="h3">迁移学习实现猫狗二分类 | 猫狗大战</h3>

    <img src="{{ url_for('static', path='img/catvsdog.png') }}" align="center"><br>

    <strong><small>支持bmp,gif,jpeg,jpg,png,ico格式图片</small></strong><br>

    <div class="buttons">
        <form method="POST" enctype="multipart/form-data" action="/v1/catvsdog/upload/">
            <input id="file" type="file" name="file" class="upload-button" title="选择图片" accept="image/bmp,image/gif,image/jpeg,image/jpg,image/png,image/x-icon"/>
            <br><br>
            <button type="submit" name="submit" class="upload-button">上传图片</button>
        </form>
    </div>
    <br>
    <small>https://www.kaggle.com/c/dogs-vs-cats/</small>
    {% include "tmpl/footer.html" ignore missing with context %}
</div>
</div>
{% endblock %}
