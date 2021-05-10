{% extends 'base.html' %}
{% block title%}{{ title }}{% endblock %}
{% block head %}
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@1.0.0/dist/tf.min.js"></script><!-- Import TensorFlow.js -->
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs-vis@1.0.2/dist/tfjs-vis.umd.min.js"></script><!-- Import tfjs-vis -->
<script src="{{ url_for('static', path='app/ml/mnist/data.js') }}" type="module"></script><!-- Import the data file -->
<script src="{{ url_for('static', path='app/ml/mnist/script.js') }}"
        type="module"></script><!-- Import the main script file -->
{% endblock %}
{% block body %}
{% block content %}
<div class="main">
    <h1 class="h1">{{ title }}</h1>
    <p align="center">
        <img alt="mnist 4" style="width: 68.50px" src="../static/img/mnist/4.png">
        <img alt="mnist 3" style="width: 67.50px" src="../static/img/mnist/3.png">
        <img alt="mnist 8" style="width: 68.50px" src="../static/img/mnist/8.png">
    </p>
    <footer>
        <small>
            &copy; 2020 <a href="https://white-album.top/">White Album</a> Made <span class="icon"
                                                                                      style="color:red">❤</span>
            By <a href="https://github.com/jamesyangget/">James Yang</a>
            <small>
                <a href="..">返回首页</a>
                <a href="javascript:void(0);" onclick="dark()">夜间模式</a>
                <a href="./policy.html">隐私政策</a>
            </small>
        </small>
    </footer>
</div>
{% endblock %}
{% endblock %}
