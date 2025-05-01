from orbit.core import orbit_mpi

mpi_comm = orbit_mpi.mpi_comm.MPI_COMM_WORLD
mpi_rank = orbit_mpi.MPI_Comm_rank(mpi_comm)
mpi_size = orbit_mpi.MPI_Comm_size(mpi_comm)

main_rank = 0

data = (1, 2, 3)
data_type = orbit_mpi.mpi_datatype.MPI_INT
data_new = orbit_mpi.MPI_Bcast(data, data_type, main_rank, mpi_comm)
print(f"rank={mpi_rank} data_new={data_new}")

data = (1.0, 2.0, 3.0)
data_type = orbit_mpi.mpi_datatype.MPI_DOUBLE
data_new = orbit_mpi.MPI_Bcast(data, data_type, main_rank, mpi_comm)
print(f"rank={mpi_rank} data_new={data_new}")

data = "test"
data_type = orbit_mpi.mpi_datatype.MPI_CHAR
data_new = orbit_mpi.MPI_Bcast(data, data_type, main_rank, mpi_comm)
print(f"rank={mpi_rank} data_new={data_new}")
