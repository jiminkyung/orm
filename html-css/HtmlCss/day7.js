
// 객체지향
const me = {
    name: "지민경",
    hometown: "춘천",
    language: "Korean",
    coding : function() {
        console.log("즐거운 코딩시간!")
    },
    studying: function(brain) {
        brain.getStress();
    }
}

const brain = {
    stress: 10,
    strength: 50,
    getStress: function() {
        this.stress++;
        this.strength--;
        console.log(`스트레스: ${this.stress}, 체력: ${this.strength}`)
    }
}

me.studying(brain);


// 생성자함수
function NewFactory(name){
    this.name = name;
    this.sayYourName = function(){
        console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
    }
}

let robot1 = new NewFactory('브랜든');


// 프로토타입
function Student(name) {
    this.name = name;
    this.stress = 10;
    this.strength = 50;
}
Student.prototype.studying = function(count) {
    this.stress += count;
    this.strength -= count;
    console.log(`${this.name}의 현재 스트레스지수는 ${this.stress}, 체력은 ${this.strength}입니다...`);
}

miwat = new Student("지민경");
miwat.studying(10);