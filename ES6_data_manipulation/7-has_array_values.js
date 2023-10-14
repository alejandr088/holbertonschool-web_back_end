const hasValuesFromArray = (set, arr) => {
    const setArray = Array.from(set);
    return arr.every((item) => setArray.includes(item));
}

export default hasValuesFromArray;
