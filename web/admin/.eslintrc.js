/*
 * @Author: Recar
 * @Date: 2019-08-15 23:38:56
 * @LastEditTime: 2019-08-15 23:59:33
 */
module.exports = {
  //默认情况下，ESLint 会在所有父级目录里寻找配置文件，一直到根目录。如果你想要你所有项目都遵循一个特定的约定时，这将会很有用，但有时候会导致意想不到的结果。为了将 ESLint 限制到一个特定的项目，在你项目根目录下的 package.json 文件或者 .eslintrc.* 文件里的 eslintConfig 字段下设置 "root": true。ESLint 一旦发现配置文件中有 "root": true，它就会停止在父级目录中寻找。
  root: true,
  parser: "babel-eslint",
  parserOptions: {
    sourceType: "module"
  },
  env: {
    browser: true
  },
  // https://github.com/standard/standard/blob/master/docs/RULES-en.md
  extends: "standard",
  // required to lint *.vue files
  plugins: ["html"],
  // add your custom rules here
  rules: {
    // 0（off）关闭规则 1（warn） 作为警告显示（不影响程序运行） 2（error） 作为错误显示（程序终止运行）
    // 要求箭头函数的参数使用圆括号
    "arrow-parens": 1,
    // allow async-await 强制 generator 函数中 * 号周围使用一致的空格
    "generator-star-spacing": 0,

    // allow debugger during development
    "no-debugger": process.env.NODE_ENV === "production" ? 2 : 0,
    indent: [0, 4], //换行时缩进4字符
    //
    "no-tabs": 2, //不允许使用制表符
    semi: 0, //语句末尾不强制使用分号
    quotes: 0, //不强制使用单引号和双引号
    "quote-props": 0, //对象字面量中的属性名不强制使用单引号和双引号
    "spaced-comment": 0, //注释风格有没有空格都可以
    eqeqeq: 2, //必须使用 “===” 和 “!==”
    "no-unused-vars": [
      1,
      {
        vars: "all",
        args: "all"
      }
    ], //不能有声明后未被使用的变量或参数
    "arrow-parens": [1, "always"],
    "comma-dangle": [
      1,
      {
        arrays: "never",
        objects: "never",
        imports: "never",
        exports: "never",
        functions: "ignore"
      }
    ], //对象或数组的最后一个元素不允许加逗号
    "no-ternary": 0, //允许使用三目运算符
    "no-trailing-spaces": 0, //一行结束后面不要有空格
    "space-infix-ops": 1, //操作符周围需要加空格
    "padded-blocks": 1, //块语句内 行首和行尾不强制要求加空行
    "brace-style": [1, "1tbs"], //块的开头大括号放置在与其相应的语句或声明相同的行上
    camelcase: [1, { properties: "always" }], //强制驼峰法命名
    "comma-spacing": [1, { before: false, after: true }], //逗号后边需要使用相同的间隙
    "space-before-function-paren": 0, //函数定义时括号前面可以没有空格
    "new-cap": 1, //构造函数名首字母必须大写
    "no-lonely-if": 1, //else代码块中不能再嵌套if语句
    "no-new-object": 1, //创建对象时不允许 new Object(),只能 使用对象字面量的方法 let obj={}
    "no-confusing-arrow": 1, //不允许这样var x = a => 1 ? 2 : 3;的写法，需要重写为var x = a => { return 1 ? 2 : 3; };
    "no-duplicate-imports": [1, { includeExports: true }], //es6中不允许重复导入模块
    "new-parens": 1, //调用没有参数的构造函数时，需要括号
    "no-unneeded-ternary": 1, //当存在更简单的替代方案时，此规则不允许三元操作符。
    "no-use-before-define": 2, //变量声明前不允许使用
    "no-undefined": 2 //不允许使用undefined为变量赋值
  }
};
