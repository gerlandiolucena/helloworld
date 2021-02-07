class HelloWorld
    attr_accessor :world, :hello
    
    def initialize()
        @world = "World"
        @hello = "Hello"
    end

    def hello()
        puts "#{@hello} #{@world}!"
    end
end

if __FILE__ == $0
    hw = HelloWorld.new
    hw.hello
end