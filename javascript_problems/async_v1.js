const getMyName = new Promise((resolve => resolve('Shampad')))
const getAge = (name) => {
    return new Promise((resolve, reject) => {
        if (name === 'Shampad') {
            resolve(21);
        } else {
            reject('Not found')
        }
    })
}

const getMyDetails = async () => {
    const name = await getMyName;
    const age = await getAge(name);
    console.log(age)
}
getMyDetails()

