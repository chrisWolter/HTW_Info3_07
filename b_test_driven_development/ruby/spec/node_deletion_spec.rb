require_relative '../node.rb'
describe Node do
  describe 'deletion' do
    context 'from a one element list' do
      # ... implement some more examples
    end
    context 'from a two element list' do
      # ... implement some more examples
    end
    context 'from a three element list' do
      let(:list) { Node.from_string('a,b,c') }
      it 'deletes first element' do
        expect(list.delete('a').to_s).to eq('b, c')
      end
      it 'deletes element in the middle'
      it 'deletes last element'
    end
  end
end
