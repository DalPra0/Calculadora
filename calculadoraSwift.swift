import SwiftUI

struct ContentView: View {
    @State private var currentInput: String = ""
    @State private var previousInput: String = ""
    @State private var operation: String = ""
    
    var body: some View {
        VStack {
            Text(currentInput.isEmpty ? "0" : currentInput)
                .font(.largeTitle)
                .padding()
                .frame(maxWidth: .infinity, alignment: .trailing)
                .background(Color.black.opacity(0.1))
            
            VStack(spacing: 10) {
                HStack(spacing: 10) {
                    Button(action: { clear() }) {
                        Text("C")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.gray)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { operationTapped("+") }) {
                        Text("+")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { operationTapped("-") }) {
                        Text("-")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                }
                
                HStack(spacing: 10) {
                    Button(action: { appendNumber("1") }) {
                        Text("1")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { appendNumber("2") }) {
                        Text("2")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { appendNumber("3") }) {
                        Text("3")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                }
                
                HStack(spacing: 10) {
                    Button(action: { appendNumber("4") }) {
                        Text("4")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { appendNumber("5") }) {
                        Text("5")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { appendNumber("6") }) {
                        Text("6")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                }
                
                HStack(spacing: 10) {
                    Button(action: { appendNumber("7") }) {
                        Text("7")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { appendNumber("8") }) {
                        Text("8")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { appendNumber("9") }) {
                        Text("9")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                }
                
                HStack(spacing: 10) {
                    Button(action: { appendNumber("0") }) {
                        Text("0")
                            .font(.title)
                            .frame(width: 160, height: 80)
                            .background(Color.blue)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { operationTapped("=") }) {
                        Text("=")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { operationTapped("/") }) {
                        Text("/")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                    
                    Button(action: { operationTapped("*") }) {
                        Text("*")
                            .font(.title)
                            .frame(width: 80, height: 80)
                            .background(Color.orange)
                            .foregroundColor(.white)
                            .cornerRadius(40)
                    }
                }
            }
            .padding()
        }
    }
    
    func appendNumber(_ number: String) {
        currentInput += number
    }
    
    func operationTapped(_ symbol: String) {
        if symbol == "=" {
            calculate()
        } else {
            operation = symbol
            previousInput = currentInput
            currentInput = ""
        }
    }
    
    func calculate() {
        let num1 = Double(previousInput) ?? 0
        let num2 = Double(currentInput) ?? 0
        var result: Double = 0
        
        switch operation {
        case "+":
            result = num1 + num2
        case "-":
            result = num1 - num2
        case "*":
            result = num1 * num2
        case "/":
            if num2 != 0 {
                result = num1 / num2
            } else {
                currentInput = "Erro"
                return
            }
        default:
            break
        }
        currentInput = String(result)
    }
    
    func clear() {
        currentInput = ""
        previousInput = ""
        operation = ""
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}

