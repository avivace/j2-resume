-- JSON parser in LuaTeX
-- Author: Henri Menke
-- Originally found at https://tex.stackexchange.com/questions/489395/error-as-i-try-to-read-and-display-the-results-from-json-file/489397#489397


local lpeg = assert(require("lpeg"))
local C, Cf, Cg, Ct, P, R, S, V =
    lpeg.C, lpeg.Cf, lpeg.Cg, lpeg.Ct, lpeg.P, lpeg.R, lpeg.S, lpeg.V

-- number parsing
local digit    = R"09"
local dot      = P"."
local eE       = S"eE"
local sign     = S"+-"^-1
local mantissa = digit^1 * dot * digit^0 + dot * digit^1 + digit^1
local exponent = (eE * sign * digit^1)^-1
local real     = sign * mantissa * exponent / tonumber

-- optional whitespace
local ws = S" \t\n\r"^0

-- match a literal string surrounded by whitespace
local lit = function(str)
    return ws * P(str) * ws
end

-- match a literal string and synthesize an attribute
local attr = function(str,attr)
    return ws * P(str) / function() return attr end * ws
end

-- JSON grammar
local json = P{
    "object",

    value =
        V"null_value" +
        V"bool_value" +
        V"string_value" +
        V"real_value" +
        V"array" +
        V"object",

    null_value =
        attr("null", nil),

    bool_value =
        attr("true", true) + attr("false", false),

    string_value =
        ws * P'"' * C((P'\\"' + 1 - P'"')^0) * P'"' * ws,

    real_value =
        ws * real * ws,

    array =
        lit"[" * Ct((V"value" * lit","^-1)^0) * lit"]",

    member_pair =
        Cg(V"string_value" * lit":" * V"value") * lit","^-1,

    object =
        lit"{" * Cf(Ct"" * V"member_pair"^0, rawset) * lit"}"
}

return { parse = function(str) return assert(json:match(str)) end }