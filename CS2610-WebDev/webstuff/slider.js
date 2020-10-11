var listSlider = function(me) {
    // the parameter 'me' refers to the <input type="slider" /> which calls this function

    // get the value from the slider

    var value = me.value;
    console.log(value);

    // Put the slider's value into the <label>
    var label = document.querySelector('#list-label');
    label.textContent = `List(${value})`;

    // Remove an existing list of numbers found in a <div> of class 'fib-list'
    var fibList = document.querySelector('div.fib-list');
    if (fibList) {
        fibList.remove();
    }

    // create a new containing <div class="fib-list">
    fibList = document.createElement('div');
    fibList.setAttribute('class', 'fib-list');

    // Using a for loop, append a list of <div class="fib-item"> containing numbers
    for (var i = 0; i <= value; i++) {
        var newDiv = document.createElement('div');
        var newP = document.createElement('p');
        newP.textContent = i;
        newDiv.appendChild(newP);
        newDiv.setAttribute('class', 'fib-item');
        fibList.appendChild(newDiv);
    }

    // finally, attach <div class="fib-list"> to the DOM
    var theForm = document.querySelector('#list-of-divs');
    theForm.appendChild(fibList);
}


var recursiveBinTree = function(depth) {
    var newDiv = document.createElement('div');
    newDiv.setAttribute('class', 'fib-item');
    var newP = document.createElement('p');
    newP.textContent = depth;
    newDiv.appendChild(newP);

    if (depth === 0) {
        return newDiv;
    }
    else {
        var left = recursiveBinTree(depth - 1);
        var cls = left.getAttribute('class');
        left.setAttribute('class', `fib-left ${cls}`);
        newDiv.appendChild(left);


        var right = recursiveBinTree(depth - 1);
        cls = right.getAttribute('class');
        right.setAttribute('class', `fib-right ${cls}`);
        newDiv.appendChild(right);

        return newDiv;
    }
}


var treeSlider = function(me) {
    // get the value from the slider
    var form = me.parentNode;

    var value = parseInt(me.value);
    console.log(value);

    // Put the slider's value into the <label>
    var label = document.querySelector('label#tree-label');
    label.textContent = `Tree(${value})`;

    // Remove an existing list of numbers found in a <div> of class 'fib-list'
    var tree = document.querySelector('#tree-of-divs');
    if (tree) {
        tree.remove();
    }

    tree = document.createElement('div');
    tree.id = 'tree-of-divs';
    tree.setAttribute('class', 'fib-container');

    var treeObj = recursiveBinTree(value);
    tree.appendChild(treeObj);

    form.parentNode.appendChild(tree);
}
