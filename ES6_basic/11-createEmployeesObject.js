export default function createEmployeesObject(departmentName, employees) {
  const newObject = {
    departmentName,
    employees
  }
  return(`{${newObject.departmentName}: [${newObject.employees}]}`)
}
