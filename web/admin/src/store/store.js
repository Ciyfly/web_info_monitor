import Vue from 'vue'

// 使用vuex
import Vuex from 'vuex'

Vue.use(Vuex)

export default  new Vuex.Store({  // 要记得挂载到 下面的vm实例上
    state:{
        // 这个相当于 data
        token: ''   // 如果在组件中想要访问 store 只能通过 this.$store.state.名称来访问
    },
    mutations:{  // 这个相当于 methoeds  如果要材质 state中的值 只能通过调用 mutations 提供的方法
        setToken(state, token){  // 如果想要调用只能  this.$store.commit('方法名')
            state.token = token;
            localStorage.setItem('token', token)
        },
        removeToken(state){
            state.token = '';
            localStorage.setItem('token', '')
        }

    },
    getters:{  // 类似组件的 compented 属性计算 
        // 不能修改数据
        getToken:function(state){
            // 这个每次 更新都会重新执行 进行计算 所有说像 compented
            return state.token;
        }
    }
})
