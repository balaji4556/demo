{"changed":true,"filter":false,"title":"day1.py","tooltip":"/day1.py","value":"from flask import Flask,render_template,request\n\n\napp= Flask(_name_)\n\n@app.route(\"/\",methods=['POST','GET'])\ndef home():\n    if request.method == 'POST':\n        num1= int(request.form['num1'])\n        num2= int(request.form['num2'])\n        num3= request.form['num3']\n        # num1=int(num1)\n        # num2=int(num2)\n        \n        if num3==\"add\":\n            sum=num1+num2\n            return render_template('home.html',output=sum)\n        elif num3==\"sub\":\n            sub=num1-num2\n            return render_template('home.html',output=sub)\n        elif num3==\"mult\":\n            mult=num1*num2\n            return render_template('home.html',output=mult)\n        elif num3==\"div\":\n            div=num1%num2\n            return render_template('home.html',output=div)\n        else:\n            return render_template('home.html',output=\"opps can't find the output\")\n        \n        # database \n       \n    return render_template('home.html')\n\n@app.route(\"/about\")\ndef about():\n    return render_template('about.html')\n@app.route(\"/blog\")\ndef blog():\n    return \"welcome to blog page\"\n@app.route(\"/login\")\ndef login():\n    return \"welcome to login page\"\n@app.route(\"/signup\")\ndef signup():\n    return \"welcome to signup page\"\n\n\n\n\n\nif _name_ == \"_main_\":\n    app.run(debug=True, host=\"0.0.0.0\")\n\n","undoManager":{"mark":92,"position":100,"stack":[[{"start":{"row":3,"column":17},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":158},{"start":{"row":4,"column":0},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":5,"column":1},"action":"insert","lines":["i"]}],[{"start":{"row":5,"column":1},"end":{"row":5,"column":2},"action":"insert","lines":["n"],"id":159},{"start":{"row":5,"column":2},"end":{"row":5,"column":3},"action":"insert","lines":["p"]},{"start":{"row":5,"column":3},"end":{"row":5,"column":4},"action":"insert","lines":["u"]},{"start":{"row":5,"column":4},"end":{"row":5,"column":5},"action":"insert","lines":["t"]},{"start":{"row":5,"column":5},"end":{"row":5,"column":6},"action":"insert","lines":["1"]}],[{"start":{"row":5,"column":6},"end":{"row":5,"column":7},"action":"insert","lines":["="],"id":160},{"start":{"row":5,"column":7},"end":{"row":5,"column":8},"action":"insert","lines":["i"]},{"start":{"row":5,"column":8},"end":{"row":5,"column":9},"action":"insert","lines":["n"]},{"start":{"row":5,"column":9},"end":{"row":5,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":10},"end":{"row":5,"column":12},"action":"insert","lines":["()"],"id":161}],[{"start":{"row":5,"column":11},"end":{"row":5,"column":12},"action":"insert","lines":["i"],"id":162},{"start":{"row":5,"column":12},"end":{"row":5,"column":13},"action":"insert","lines":["n"]},{"start":{"row":5,"column":13},"end":{"row":5,"column":14},"action":"insert","lines":["p"]},{"start":{"row":5,"column":14},"end":{"row":5,"column":15},"action":"insert","lines":["u"]},{"start":{"row":5,"column":15},"end":{"row":5,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":5,"column":16},"end":{"row":5,"column":18},"action":"insert","lines":["()"],"id":163}],[{"start":{"row":5,"column":17},"end":{"row":5,"column":19},"action":"insert","lines":["\"\""],"id":164}],[{"start":{"row":5,"column":18},"end":{"row":5,"column":19},"action":"insert","lines":["e"],"id":165},{"start":{"row":5,"column":19},"end":{"row":5,"column":20},"action":"insert","lines":["n"]},{"start":{"row":5,"column":20},"end":{"row":5,"column":21},"action":"insert","lines":["t"]},{"start":{"row":5,"column":21},"end":{"row":5,"column":22},"action":"insert","lines":["e"]},{"start":{"row":5,"column":22},"end":{"row":5,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":5,"column":23},"end":{"row":5,"column":24},"action":"insert","lines":[" "],"id":166},{"start":{"row":5,"column":24},"end":{"row":5,"column":25},"action":"insert","lines":["a"]}],[{"start":{"row":5,"column":25},"end":{"row":5,"column":26},"action":"insert","lines":[" "],"id":167},{"start":{"row":5,"column":26},"end":{"row":5,"column":27},"action":"insert","lines":["v"]},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["A"]}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["A"],"id":168}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["A"],"id":169},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["L"]}],[{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"remove","lines":["L"],"id":170},{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"remove","lines":["A"]}],[{"start":{"row":5,"column":27},"end":{"row":5,"column":28},"action":"insert","lines":["a"],"id":171},{"start":{"row":5,"column":28},"end":{"row":5,"column":29},"action":"insert","lines":["l"]},{"start":{"row":5,"column":29},"end":{"row":5,"column":30},"action":"insert","lines":["u"]},{"start":{"row":5,"column":30},"end":{"row":5,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":[","],"id":172}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":[","],"id":173}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":[":"],"id":174}],[{"start":{"row":5,"column":35},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":175},{"start":{"row":6,"column":0},"end":{"row":6,"column":1},"action":"insert","lines":["i"]},{"start":{"row":6,"column":1},"end":{"row":6,"column":2},"action":"insert","lines":["n"]},{"start":{"row":6,"column":2},"end":{"row":6,"column":3},"action":"insert","lines":["p"]}],[{"start":{"row":6,"column":3},"end":{"row":6,"column":4},"action":"insert","lines":["u"],"id":176},{"start":{"row":6,"column":4},"end":{"row":6,"column":5},"action":"insert","lines":["t"]},{"start":{"row":6,"column":5},"end":{"row":6,"column":6},"action":"insert","lines":["2"]}],[{"start":{"row":6,"column":6},"end":{"row":6,"column":7},"action":"insert","lines":["="],"id":177},{"start":{"row":6,"column":7},"end":{"row":6,"column":8},"action":"insert","lines":["i"]},{"start":{"row":6,"column":8},"end":{"row":6,"column":9},"action":"insert","lines":["n"]},{"start":{"row":6,"column":9},"end":{"row":6,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":10},"end":{"row":6,"column":12},"action":"insert","lines":["()"],"id":178}],[{"start":{"row":6,"column":11},"end":{"row":6,"column":12},"action":"insert","lines":["i"],"id":179},{"start":{"row":6,"column":12},"end":{"row":6,"column":13},"action":"insert","lines":["n"]},{"start":{"row":6,"column":13},"end":{"row":6,"column":14},"action":"insert","lines":["p"]},{"start":{"row":6,"column":14},"end":{"row":6,"column":15},"action":"insert","lines":["u"]},{"start":{"row":6,"column":15},"end":{"row":6,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":6,"column":16},"end":{"row":6,"column":18},"action":"insert","lines":["()"],"id":180}],[{"start":{"row":6,"column":17},"end":{"row":6,"column":19},"action":"insert","lines":["\"\""],"id":181}],[{"start":{"row":6,"column":18},"end":{"row":6,"column":19},"action":"insert","lines":["e"],"id":182},{"start":{"row":6,"column":19},"end":{"row":6,"column":20},"action":"insert","lines":["n"]},{"start":{"row":6,"column":20},"end":{"row":6,"column":21},"action":"insert","lines":["t"]},{"start":{"row":6,"column":21},"end":{"row":6,"column":22},"action":"insert","lines":["e"]},{"start":{"row":6,"column":22},"end":{"row":6,"column":23},"action":"insert","lines":["r"]}],[{"start":{"row":6,"column":23},"end":{"row":6,"column":24},"action":"insert","lines":[" "],"id":183},{"start":{"row":6,"column":24},"end":{"row":6,"column":25},"action":"insert","lines":["b"]}],[{"start":{"row":6,"column":25},"end":{"row":6,"column":26},"action":"insert","lines":[" "],"id":184},{"start":{"row":6,"column":26},"end":{"row":6,"column":27},"action":"insert","lines":["v"]},{"start":{"row":6,"column":27},"end":{"row":6,"column":28},"action":"insert","lines":["a"]},{"start":{"row":6,"column":28},"end":{"row":6,"column":29},"action":"insert","lines":["l"]},{"start":{"row":6,"column":29},"end":{"row":6,"column":30},"action":"insert","lines":["u"]},{"start":{"row":6,"column":30},"end":{"row":6,"column":31},"action":"insert","lines":["e"]}],[{"start":{"row":6,"column":32},"end":{"row":6,"column":33},"action":"insert","lines":[":"],"id":185}],[{"start":{"row":6,"column":35},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":186},{"start":{"row":7,"column":0},"end":{"row":8,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":1},"action":"insert","lines":["p"],"id":187},{"start":{"row":8,"column":1},"end":{"row":8,"column":2},"action":"insert","lines":["r"]},{"start":{"row":8,"column":2},"end":{"row":8,"column":3},"action":"insert","lines":["i"]},{"start":{"row":8,"column":3},"end":{"row":8,"column":4},"action":"insert","lines":["n"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"insert","lines":[")"],"id":188}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":[")"],"id":189}],[{"start":{"row":8,"column":5},"end":{"row":8,"column":7},"action":"insert","lines":["()"],"id":190}],[{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"insert","lines":["i"],"id":191},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"insert","lines":["n"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"insert","lines":["p"]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"insert","lines":["u"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["1"],"id":192}],[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["*"],"id":193}],[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["i"],"id":194},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["n"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["p"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["u"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["t"]}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["2"],"id":195}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":196}],[{"start":{"row":5,"column":0},"end":{"row":6,"column":0},"action":"remove","lines":["",""],"id":197}],[{"start":{"row":5,"column":35},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":198}],[{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"remove","lines":[":"],"id":199}],[{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"remove","lines":[":"],"id":200}],[{"start":{"row":7,"column":31},"end":{"row":7,"column":32},"action":"insert","lines":[" "],"id":201},{"start":{"row":7,"column":32},"end":{"row":7,"column":33},"action":"insert","lines":[":"]}],[{"start":{"row":5,"column":31},"end":{"row":5,"column":32},"action":"insert","lines":[" "],"id":202},{"start":{"row":5,"column":32},"end":{"row":5,"column":33},"action":"insert","lines":[":"]}],[{"start":{"row":9,"column":20},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":203},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["f"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["o"]}],[{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["r"],"id":204}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":[" "],"id":205},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["i"]}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":[" "],"id":206},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["i"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":["n"]}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":[" "],"id":207},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["r"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["a"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":["n"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["h"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["e"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["e"],"id":208},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["h"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":["n"]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["a"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["r"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"remove","lines":[" "]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"remove","lines":["n"]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"remove","lines":["i"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"remove","lines":[" "]}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":["i"],"id":209},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"remove","lines":[" "]}],[{"start":{"row":11,"column":3},"end":{"row":12,"column":0},"action":"insert","lines":["",""],"id":210},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"insert","lines":["i"]},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":["n"]}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["\\"],"id":211}],[{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"remove","lines":["\\"],"id":212},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":["n"]}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[" "],"id":213}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":[" "],"id":214}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":["="],"id":215}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":["="],"id":216}],[{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"insert","lines":[" "],"id":217},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"insert","lines":["="]}],[{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"insert","lines":[" "],"id":218},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"insert","lines":["1"]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"insert","lines":["0"]}],[{"start":{"row":12,"column":6},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":219}],[{"start":{"row":12,"column":6},"end":{"row":13,"column":0},"action":"remove","lines":["",""],"id":220}],[{"start":{"row":12,"column":6},"end":{"row":13,"column":0},"action":"insert","lines":["",""],"id":221},{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["",""],"id":222},{"start":{"row":12,"column":6},"end":{"row":13,"column":0},"action":"remove","lines":["",""]},{"start":{"row":12,"column":5},"end":{"row":12,"column":6},"action":"remove","lines":["0"]},{"start":{"row":12,"column":4},"end":{"row":12,"column":5},"action":"remove","lines":["1"]},{"start":{"row":12,"column":3},"end":{"row":12,"column":4},"action":"remove","lines":[" "]},{"start":{"row":12,"column":2},"end":{"row":12,"column":3},"action":"remove","lines":["="]},{"start":{"row":12,"column":1},"end":{"row":12,"column":2},"action":"remove","lines":[" "]},{"start":{"row":12,"column":0},"end":{"row":12,"column":1},"action":"remove","lines":["i"]},{"start":{"row":11,"column":3},"end":{"row":12,"column":0},"action":"remove","lines":["",""]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"remove","lines":["r"]}],[{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"remove","lines":["o"],"id":223},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["f"]},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":224}],[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["f"],"id":225},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"insert","lines":["o"]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"insert","lines":["r"]}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"insert","lines":[" "],"id":226}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"remove","lines":[" "],"id":227}],[{"start":{"row":11,"column":3},"end":{"row":11,"column":5},"action":"insert","lines":["()"],"id":228}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["1"],"id":229}],[{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"insert","lines":["="],"id":230}],[{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"insert","lines":["5"],"id":231}],[{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"insert","lines":[","],"id":232}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":["1"],"id":233}],[{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"insert","lines":["i"],"id":234}],[{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"insert","lines":["i"],"id":235}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["="],"id":236}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["="],"id":237}],[{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"insert","lines":["+"],"id":238},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"insert","lines":["1"]}],[{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"insert","lines":[","],"id":239},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"insert","lines":["i"]}],[{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"insert","lines":["+"],"id":240},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"insert","lines":["+"]}],[{"start":{"row":11,"column":15},"end":{"row":11,"column":16},"action":"remove","lines":[")"],"id":241},{"start":{"row":11,"column":14},"end":{"row":11,"column":15},"action":"remove","lines":["+"]},{"start":{"row":11,"column":13},"end":{"row":11,"column":14},"action":"remove","lines":["+"]},{"start":{"row":11,"column":12},"end":{"row":11,"column":13},"action":"remove","lines":["i"]},{"start":{"row":11,"column":11},"end":{"row":11,"column":12},"action":"remove","lines":[","]},{"start":{"row":11,"column":10},"end":{"row":11,"column":11},"action":"remove","lines":["1"]},{"start":{"row":11,"column":9},"end":{"row":11,"column":10},"action":"remove","lines":["+"]},{"start":{"row":11,"column":8},"end":{"row":11,"column":9},"action":"remove","lines":["i"]},{"start":{"row":11,"column":7},"end":{"row":11,"column":8},"action":"remove","lines":[","]},{"start":{"row":11,"column":6},"end":{"row":11,"column":7},"action":"remove","lines":["5"]},{"start":{"row":11,"column":5},"end":{"row":11,"column":6},"action":"remove","lines":["="]},{"start":{"row":11,"column":4},"end":{"row":11,"column":5},"action":"remove","lines":["i"]},{"start":{"row":11,"column":3},"end":{"row":11,"column":4},"action":"remove","lines":["("]},{"start":{"row":11,"column":2},"end":{"row":11,"column":3},"action":"remove","lines":["r"]},{"start":{"row":11,"column":1},"end":{"row":11,"column":2},"action":"remove","lines":["o"]},{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["f"]},{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"remove","lines":["",""]},{"start":{"row":9,"column":20},"end":{"row":10,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":9,"column":20},"end":{"row":10,"column":0},"action":"insert","lines":["",""],"id":242}],[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""],"id":243}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"remove","lines":["6"],"id":244}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":19},"action":"insert","lines":["\"\""],"id":245}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["a"],"id":246}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"remove","lines":["a"],"id":247}],[{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["b"],"id":248},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["a"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["l"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["a"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["j"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["i"]}],[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["4"],"id":249},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":[":"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["0"]}],[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["5"],"id":250}],[{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"insert","lines":["g"],"id":251},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"insert","lines":["i"]}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":[" "],"id":252}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":[" "],"id":253}],[{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"insert","lines":["t"],"id":254}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"insert","lines":[" "],"id":255}],[{"start":{"row":9,"column":23},"end":{"row":9,"column":24},"action":"remove","lines":[" "],"id":256},{"start":{"row":9,"column":22},"end":{"row":9,"column":23},"action":"remove","lines":["t"]},{"start":{"row":9,"column":21},"end":{"row":9,"column":22},"action":"remove","lines":["i"]},{"start":{"row":9,"column":20},"end":{"row":9,"column":21},"action":"remove","lines":["g"]}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":20},"action":"remove","lines":["list1=[1,2,3,4,5,\"balaji\",7,8,9,10]","print(list1)","","print(list1[5])","","input1=int(input(\"enter a value :\"))","","input2=int(input(\"enter b value :\"))","","print(input1*input2)"],"id":258}],[{"start":{"row":0,"column":0},"end":{"row":51,"column":39},"action":"insert","lines":["from flask import Flask,render_template,request","","","app= Flask(_name_)","","@app.route(\"/\",methods=['POST','GET'])","def home():","    if request.method == 'POST':","        num1= int(request.form['num1'])","        num2= int(request.form['num2'])","        num3= request.form['num3']","        # num1=int(num1)","        # num2=int(num2)","        ","        if num3==\"add\":","            sum=num1+num2","            return render_template('home.html',output=sum)","        elif num3==\"sub\":","            sub=num1-num2","            return render_template('home.html',output=sub)","        elif num3==\"mult\":","            mult=num1*num2","            return render_template('home.html',output=mult)","        elif num3==\"div\":","            div=num1%num2","            return render_template('home.html',output=div)","        else:","            return render_template('home.html',output=\"opps can't find the output\")","        ","        # database ","       ","    return render_template('home.html')","","@app.route(\"/about\")","def about():","    return render_template('about.html')","@app.route(\"/blog\")","def blog():","    return \"welcome to blog page\"","@app.route(\"/login\")","def login():","    return \"welcome to login page\"","@app.route(\"/signup\")","def signup():","    return \"welcome to signup page\"","","","","","","if _name_ == \"_main_\":","    app.run(debug=True, host=\"0.0.0.0\")"],"id":259}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":51,"column":39},"end":{"row":51,"column":39},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1718608446513}