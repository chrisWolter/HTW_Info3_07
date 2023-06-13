require_relative '../node.rb'
describe Node do
  describe 'is an Enumeration' do
    it 'implements each' do
      origin = 'a, b, c, d'
      list = Node.from_string(origin)
      a = []
      list.each do |e|
        a << e
      end
      expect(a.join(', ')).to eq origin
    end
  end
end
