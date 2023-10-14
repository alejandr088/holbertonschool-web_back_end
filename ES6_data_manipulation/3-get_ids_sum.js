const getStudentsIdsSum = (students) => {
    if (!Array.isArray(students)) {
        return [];
    }

    return students.reduce((accum, currentVal) => accum + currentVal.id, 0);
}

export default getStudentsIdsSum;
