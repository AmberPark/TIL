// Class

function Car(options) {
  this.title = options.title

  this.drive = function () {
    return '부릉부릉'
  }
}

options = {title: 'bmw', color:'blue'}

const car = new Car(options)
car.title
car.drive()
