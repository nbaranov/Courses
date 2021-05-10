import { revertString } from "../revertString.js";

describe("tests for revertString function", () => {
    it("should reverse string", () => {
        expect(revertString("abc")).toBe("cba")
        expect(revertString("123")).toBe("321")
        expect(revertString("qwerty")).toBe("ytrewq")
    })
});