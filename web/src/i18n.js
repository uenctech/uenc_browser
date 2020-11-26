import Vue from "vue";
import locale from "element-ui/lib/locale";
import VueI18n from "vue-i18n";
import messages from "./i18n/index";

Vue.use(VueI18n);
const i18n = new VueI18n({
  locale: localStorage.lang || "cn",
  messages
});
locale.i18n((key, value) => i18n.t(key, value));
export default i18n;
