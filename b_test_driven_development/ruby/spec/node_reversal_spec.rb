require_relative '../node.rb'
describe 'Node reverses' do
  it 'a one element list' do
    pending
    list = Node.from_string('c')
    expect(list.reverse.to_s).to eq 'c'
  end
  it 'a two element list' do
    pending
    list = Node.from_string('A,B')
    expect(list.reverse.to_s).to eq 'B, A'
  end
  it 'a many element list' do
    pending
    list = Node.from_string('A,B,C,D,E,F')
    expect(list.reverse.to_s).to eq 'F, E, D, C, B, A'
  end
end
