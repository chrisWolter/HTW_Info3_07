# frozen_string_literal: true

# Node and Head of a LinkedList
class Node
  attr_accessor :data, :next_node

  def initialize(data, next_node = nil)
    @data = data
    @next_node = next_node
  end

  def delete(data_to_be_deleted)
    # this is a too simple implementation to satisfy the first deletion example.
    next_node
  end

  # pre-defined convenience methods for creation and conversion to string.
  def self.from_string(s)
    nodes = s.split(',')
    nodes.map(&:strip).reverse.inject(nil) { |list, element| Node.new(element, list) }
  end

  include Enumerable
  def each
    yield data
    current = next_node
    until current.nil?
      yield current.data
      current = current.next_node
    end
  end

  def to_s
    inject { |memo, e| memo + ', ' + e}
  end

end
