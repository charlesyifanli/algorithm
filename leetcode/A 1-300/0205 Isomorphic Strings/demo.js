/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
let isIsomorphic = function (s, t) {
    let dict = {}
    for (let i = 0; i < s.length; i++) {
        if (!(s[i] in dict)) {
            if (Object.values(dict).includes(t[i])) return false
            dict[s[i]] = t[i]
        } else if (dict[s[i]] !== t[i]) {
            return false
        }
    }
    return true
}
