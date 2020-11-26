import Vue from "vue";
import VueRouter from "vue-router";
Vue.use(VueRouter);
// const originalPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push(location) {
//     return originalPush.call(this, location).catch(err => err)
// }
// const routerPush = VueRouter.prototype.push
// VueRouter.prototype.push = function push(location) {
//   return routerPush.call(this, location).catch(error=> error)
// }

const routes = [{
    path: "/",
    component: () =>
        import("../views/Home.vue"),
    children: [{
        path: '/',
        name: 'index',
        component: () =>
            import("../views/Index.vue"),
        meta: {
            keepAlive: true // 需要被缓存
        }
    },
    {
        path: "/address",
        name: "addressed",
        component: () =>
            import("../views/Address.vue"),
        meta: {
            keepAlive: true // 需要被缓存
        },

    },
    {
        path: '/block',
        name: 'block',
        component: () =>
            import("../views/Block.vue"),
        meta: {
            keepAlive: true // 需要被缓存
        }

    },
    {
        path: "/transaction",
        name: "transaction",
        component: () =>
            import("../views/Transaction.vue"),
        meta: {
            keepAlive: true // 需要被缓存
        }
    },
    // 区块详情页
    {
        path: "/blockdetail",
        name: "blockdetail",
        component: () =>
            import("../views/blockchildren/blockdetail.vue"),
        meta: {
            keepAlive: false // 需要被缓存
        }
    },
    // 区块详情页2
    {
        path: "/blockdetails",
        name: "blockdetails",
        component: () =>
            import("../views/blockchildren/blockdetails.vue"),
        meta: {
            keepAlive: false // 需要被缓存
        }
    },

    // 交易详情页
    {
        path: "/transactiondetail",
        name: "transactiondetail",
        component: () =>
            import("../views/transactionchildren/transactiondetail.vue"),
        meta: {
            keepAlive: false// 需要被缓存
        }
    },
    // 地址搜索详情页
    {
        path: "/transactiondetails",
        name: "transactiondetails",
        component: () =>
            import("../views/transactionchildren/transactiondetails.vue"),
        meta: {
            keepAlive: false // 需要被缓存
        }
    },
    {
        path: "/notfound",
        name: "notfound",
        component: () =>
            import("../views/notfound.vue"),
        meta: {
            keepAlive: false // 需要被缓存
        }
    },
    {
        path: "/not",
        name: "not",
        component: () =>
            import("../views/not.vue"),
        meta: {
            keepAlive: false // 需要被缓存
        }
    },
    ]
},
    // // 搜索栏
    // {
    //     path: "/search",
    //     name: "search",
    //     component: () =>
    //         import("../components/common/search.vue"),
    //     meta: {
    //         keepAlive: false // 需要被缓存
    //     }
    // },
    // 搜索栏

];

const router = new VueRouter({
    routes,
});
export default router;